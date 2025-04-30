package TOClean;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class CanvasUndoRedo {
}

class Operation {
    int x;
    int y;
    String valueSet;
    String valuePrev;

    public Operation(int x, int y, String valueSet, String valuePrev) {
        this.x = x;
        this.y = y;
        this.valueSet = valueSet;
        this.valuePrev = valuePrev;
    }

    public String toString() {
        return "x: " + x + " y: "  + y + " valueSet: " + valueSet + " valuePrev: " + valuePrev;
    }
}

class Canvas {
    String[][] coordinates;
    Stack<Operation> operationsUndo;
    Stack<Operation> operationsRedo;

    public Canvas(int width, int height) {
        coordinates = new String[height][width];
        operationsUndo = new Stack<Operation>();
        operationsRedo = new Stack<Operation>();
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < coordinates.length; i++) {
            for (int j = 0; j < coordinates[j].length; j++) {
                sb.append(coordinates[i][j]);
                sb.append(",");
            }
            sb.append("\n");
        }

        List<Operation> ops = new ArrayList<Operation>(operationsUndo);

        for (Operation op: ops) {
            sb.append(op.toString());
            sb.append("\n");
        }

        return sb.toString();
    }

    public void setPixel(int x, int y, String val) {
        if (x < 0 ||
            x >= coordinates.length ||
            y < 0 ||
            y >= coordinates[x].length) {
            throw new IllegalArgumentException ("co-ordinate index out of bounds");
        }

        operationsUndo.push(new Operation(x, y, val, coordinates[x][y]));
        operationsRedo.removeAllElements();
        coordinates[x][y] = val;
    }

    public void undo() {
        if (operationsUndo.size() > 0) {
            Operation op = operationsUndo.pop();
            coordinates[op.x][op.y] = op.valuePrev;
            operationsRedo.push(op);
        }
    }

    public void redo() {
        if (operationsRedo.size() > 0) {
            Operation op = operationsRedo.pop();
            coordinates[op.x][op.y] = op.valueSet;
            operationsUndo.push(op);
        }
    }

    public boolean isRedoPossible() {
        return operationsRedo.size() != 0;
    }
}


class MyCode {
    public static void main (String[] args) {
        Canvas c = new Canvas(10, 15);
        c.setPixel(0, 0, "test0_0");
        c.setPixel(14, 9, "test9_14");
        // c.setPixel(15, 12, "test");
//    System.out.println(c);
        c.undo();
        c.undo();

//    System.out.println(c);
        c.redo();
        c.redo();
//    System.out.println(c);

        try {
            c.setPixel(15, 9, "test9_15");
        } catch (Exception ex) {
            System.out.println("Error updating:" + ex.toString());
        }
    }
}


// Your last Plain Text code is saved below:

// 1. make canvas - specified width and height
// 2. paint a pixel a color
// 3. undo
// 4. redo



// [x,y] = "ABC"; U_S: "null" -> "ABC"
// [x,y] = "CED"; U_S: "ABC" -> "CED", "null" -> "ABC"
// undo
// [x,y] = "ACB"; U_S: "null" -> "ABC" R_S: "ABC" -> "CED"
// [x,y] = "DEF"; U_S: "ABC" -> "DEF", "null" -> "ABC" R_S: "ABC" -> "CED"



