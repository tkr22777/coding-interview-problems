package TOClean;

import java.util.Stack;

/* https://leetcode.com/problems/implement-queue-using-stacks/ */
/**
 * Your MyQueue object will be instantiated and called as such:
 * QueueUsingStack obj = new QueueUsingStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */

class QueueUsingStack {

    /* Explanation:
            Q: In -> - -> Out
            Stk1 In/Out -> -,
            Stk2 In/Out -> -,

     push 1, Q: In -> 1 -> Out

            Stk1 In/Out -> 1,
            Stk2 In/Out -> -,

     push 2, Q: In -> 2, 1 -> Out
            Stk1 In/Out -> 1
            Stk2 In/Out -> -

         2
            Stk1 In/Out -> 1
            Stk2 In/Out -> -

            Stk1 In/Out -> 2, 1
            Stk2 In/Out -> -

     //when a peek happens, if stk2 is not empty return from stk2, otherwise move all one by one from stck 1 to stk2 and return empty, this make the retrival runtime a bit slow
            Stk1 In/Out -> -
            Stk2 In/Out -> 1, 2


     push 3, Q: In -> 3, 2, 1 -> Out
         3
            Stk1 In/Out -> -
            Stk2 In/Out -> 1, 2

            Stk1 In/Out -> 3
            Stk2 In/Out -> 1, 2

     pop, 1
            Stk1 In/Out -> 3
            Stk2 In/Out -> 2

     push 4, Q: In -> 4, 3, 2 -> Out
         4
            Stk1 In/Out -> 3
            Stk2 In/Out -> 2

            Stk1 In/Out -> 4, 3
            Stk2 In/Out -> 2


     pop 2,
            Stk1 In/Out -> 4, 3
            Stk2 In/Out ->

     pop 3,
            Stk1 In/Out -> 3
            Stk2 In/Out -> 4

            Stk1 In/Out ->
            Stk2 In/Out -> 3, 4

            Stk1 In/Out ->
            Stk2 In/Out -> 4
    */

    Stack<Integer> stk1;
    Stack<Integer> stk2;

    public QueueUsingStack() {
        stk1 = new Stack<Integer>();
        stk2 = new Stack<Integer>();
    }

    public void push(int x) {
        stk1.push(x);
    }

    public int pop() {
        if(!stk2.isEmpty()) {
            return stk2.pop();
        }

        moveToStk2();

        if(!stk2.isEmpty()) {
            return stk2.pop();
        }
        return -1;
    }

    public int peek() {
        if(!stk2.isEmpty()) {
            return stk2.peek();
        }

        moveToStk2();


        if(!stk2.isEmpty()) {
            return stk2.peek();
        }

        return -1;
    }

    public boolean empty() {
        return stk1.isEmpty() && stk2.isEmpty();
    }

    private void moveToStk2() {
        while(!stk1.isEmpty()) {
            stk2.push(stk1.pop());
        }
    }
}
