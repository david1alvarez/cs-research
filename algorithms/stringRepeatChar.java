// The following has a time complexity of O(n) with a max of 128
boolean isUniqueCharsBooleanArrayComparison(String str) {
    if (str.length() > 128) { // assumes standard ASCII characters
        return false; // pigeonhole theory
    }

    boolean[] char_set = new boolean[128];
    for (int i = 0; i < str.length(); i++) {
        int val = str.charAt(i);
        if (char_set[val]) { // value previously set to true, indicates duplicate letter
            return false;
        }
        char_set[val] = true;
    }
}

boolean isUniqueCharsBitVector(String str) {
    int checker = 0;
    for (int i = 0; i < str.length(); i++) {
        int val = str.charAt(i) - 'a';
        if ((checker & (1 << val)) > 0) {
            return false;
        }
        checker |= (1 << val);
    }
    return true;
}