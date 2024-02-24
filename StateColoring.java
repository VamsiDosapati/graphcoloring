import java.util.*;

public class GraphColoring {
    public static Map<String, String> coloring(Map<String, List<String>> graph, List<String> colors) {
        Map<String, String> assignment = new HashMap<>();
        String startState = graph.keySet().iterator().next(); // Start from the first state
        if (backtrack(assignment, startState, graph, colors)) {
            return assignment;
        } else {
            return null;
        }
    }

    public static boolean isSafe(String state, String color, Map<String, String> assignment, Map<String, List<String>> graph) {
        for (String neighbor : graph.get(state)) {
            if (assignment.containsKey(neighbor) && assignment.get(neighbor).equals(color)) {
                return false;
            }
        }
        return true;
    }

    public static boolean backtrack(Map<String, String> assignment, String state, Map<String, List<String>> graph, List<String> colors) {
        if (state == null) {
            return true; // All states are colored
        }
        for (String color : colors) {
            if (isSafe(state, color, assignment, graph)) {
                assignment.put(state, color);
                String nextState = getNextUncolored(assignment, graph);
                if (backtrack(assignment, nextState, graph, colors)) {
                    return true;
                }
                assignment.remove(state); // Backtrack
            }
        }
        return false;
    }

    public static String getNextUncolored(Map<String, String> assignment, Map<String, List<String>> graph) {
        for (String state : graph.keySet()) {
            if (!assignment.containsKey(state)) {
                return state;
            }
        }
        return null;
    }

    public static void main(String[] args) {
        Map<String, List<String>> contiguousUSGraph = new HashMap<>();
        // Define the adjacency relationships between states (same as in Python code)
        contiguousUSGraph.put("WA", Arrays.asList("ID", "OR"));
        contiguousUSGraph.put("ID", Arrays.asList("WA", "MT", "OR", "NV", "UT", "WY"));
        contiguousUSGraph.put("MT", Arrays.asList("ID", "ND", "SD", "WY"));
        contiguousUSGraph.put("ND", Arrays.asList("MT", "SD", "MN"));
        contiguousUSGraph.put("SD", Arrays.asList("MT", "ND", "WY", "NE", "IA", "MN"));
        // Add other state adjacency relationships here...

        List<String> colors = Arrays.asList("R", "G", "B", "Y");
        Map<String, String> stateColors = coloring(contiguousUSGraph, colors);

        if (stateColors != null) {
            System.out.println("State  Color");
            for (Map.Entry<String, String> entry : stateColors.entrySet()) {
                System.out.printf("%-5s - %s%n", entry.getKey(), entry.getValue());
            }
        } else {
            System.out.println("No valid coloring found.");
        }
    }
}
