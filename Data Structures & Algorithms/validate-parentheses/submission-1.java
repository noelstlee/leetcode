class Solution {
    public boolean isValid(String s) {
        // iterate through the string
        // check if the bracket is the new type that hasn't been seen
        // if it hasn't been seen --> could continue until we get the full bracket 
        // if not full bracket found -- invalid
        // if full bracket found -- then pop from stack for the seen brakckets' closing ones
        // if not all of them found --> return false

        java.util.Deque<Character> st = new java.util.ArrayDeque<>();

        for (int i = 0 ; i < s.length(); i++) {
            char c = s.charAt(i);

            if ( c == '(') {
                st.push(')');
            } else if (c == '{') {
                st.push('}');
            } else if (c == '[') {
                st.push(']');

            } else {
                // we encountered a closing bracket 
                if (st.isEmpty()) {
                    return false;
                }

                char n = st.pop();
                if (c != n) {
                    return false;
                }
            }
        }
        // valid only if we matched every opener brackets!
        return st.isEmpty();
    }
}
