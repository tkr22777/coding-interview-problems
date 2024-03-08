import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;

// https://leetcode.com/problems/exclusive-time-of-functions/description/

public class ExclusiveTimeOfFunctions {

    public static void main(String[] args) {
        int n = 2;
        String[] logs_array = {"0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"};
        List<String> logs = new ArrayList<>(List.of(logs_array));
        int[] output = exclusiveTime(n, logs);
        System.out.println("ExTime:" + Arrays.toString(output));
    }

    static class TaskState {
        int id;
        String state;
        int timestamp;

        public TaskState(int id, String state, int ts) {
            this.id = id;
            this.state = state;
            this.timestamp = ts;
        }
    }

    public static int[] exclusiveTime(int n, List<String> logs) {

        Stack<TaskState> taskStateStack = new Stack<>();
        int[] task_duration = new int[n];

        for (String log: logs) {
            TaskState ts = toTaskState(log);
            //System.out.println(ts);

            if (ts.state.equals("start")) {
                taskStateStack.push(ts);
            } else if (ts.state.equals("end")) {
                TaskState poppedTs = taskStateStack.pop();
                int duration = ts.timestamp - poppedTs.timestamp + 1;
                task_duration[ts.id] += duration;
                // the following is the most tricky part of the problem
                // here the current tasks duration is subtracted from the
                // calling functions duration
                if (!taskStateStack.isEmpty()) {
                    task_duration[taskStateStack.peek().id] -= duration;
                }
            }
        }
        return task_duration;
    }

    public static TaskState toTaskState(String log) {
        String[] log_parts = log.split(":");
        return new TaskState(Integer.parseInt(log_parts[0]), log_parts[1], Integer.parseInt(log_parts[2]));
    }
}
