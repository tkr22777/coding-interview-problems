package sync;

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

class Job {
    String id;
    public Job(String id) {  this.id = id; }
    boolean ranPhase1 = false;
    boolean ranPhase2 = false;
    boolean ranPhase3 = false;

    public void executePhase1() {
        synchronized (this) {
            if (!ranPhase1) {
                System.out.println(String.format("Job[%s] executed phase 1.", id));
                ranPhase1 = true;
            } else {
                System.out.println(String.format("Job[%s] phase 1 already ran", id));
            }
        }
    }

    public void executePhase2() {
        while (!ranPhase1) {
            try {
                Thread.sleep(10);
            } catch (InterruptedException e) {
                System.out.println(String.format("Job[%s] Exception while trying to sleep in phase 2", id));
            }
        }
        synchronized (this) {
            if (!ranPhase2) {
                System.out.println(String.format("Job[%s] executed phase 2.", id));
                ranPhase2 = true;
            } else {
                System.out.println(String.format("Job[%s] phase 2 already ran", id));
            }
        }
    }

    public void executePhase3() {
        while (!ranPhase2) {
            try {
                Thread.sleep(10);
            } catch (InterruptedException e) {
                System.out.println(String.format("Job[%s] Exception while trying to sleep in phase 3", id));
            }
        }
        synchronized (this) {
            if (!ranPhase3) {
                System.out.println(String.format("Job[%s] executed phase 3.", id));
                ranPhase3 = true;
            } else {
                System.out.println(String.format("Job[%s] phase 3 already ran", id));
            }
        }
    }
}

class JobRunner implements Runnable  {
    Job job;
    public JobRunner(Job j) {
        this.job = j;
    }

    @Override
    public void run() { }
}

class Phase1Runner extends JobRunner implements Runnable {
    public Phase1Runner(Job j) { super(j); }
    @Override
    public void run() {
        job.executePhase1();
    }
}

class Phase2Runner extends JobRunner implements Runnable {
    public Phase2Runner(Job j) { super(j); }
    @Override
    public void run() {
        job.executePhase2();
    }
}

class Phase3Runner extends JobRunner implements Runnable {
    public Phase3Runner(Job j) { super(j); }
    @Override
    public void run() {
        job.executePhase3();
    }
}

class NotSoSmartJobScheduler {
    LinkedList<Job> jobs = new LinkedList<>();

    public NotSoSmartJobScheduler(List<Job> jobs) {
        for (Job j: jobs) {
            this.jobs.add(j);
        }
    }

    public void exec() {
        List<JobRunner> runners = new ArrayList<>();
        for (Job j: jobs) {
            runners.add(new Phase1Runner(j));
            runners.add(new Phase2Runner(j));
            runners.add(new Phase3Runner(j));
            // here the scheduler is being not so smart and preparing some redundant runner instances
            int rand = ((int)(Math.random() * 18) % 3) + 1;
            switch (rand) {
                case 1:
                    runners.add(new Phase2Runner(j));
                    runners.add(new Phase3Runner(j));
                case 2:
                    runners.add(new Phase1Runner(j));
                    runners.add(new Phase3Runner(j));
                case 3:
                    runners.add(new Phase1Runner(j));
                    runners.add(new Phase2Runner(j));
            }
        }
        Collections.shuffle(runners);

        for (JobRunner jr: runners) {
            new Thread(jr).start();
        }
    }
}

public class Pilot {
    public static void main(String[] args) {
        List<Job> jobs = new ArrayList<>();
        for (int i = 0; i < 5; i++) {
            jobs.add(new Job(String.format("00%d", i)));
        }
        NotSoSmartJobScheduler jEx = new NotSoSmartJobScheduler(jobs);
        jEx.exec();
    }
}
