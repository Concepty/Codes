package test_closure;

interface OneMethodInterface {
    public int operation(String str1, String str2);
}

class MainClass {
    public void exec(OneMethodInterface i1, OneMethodInterface i2, String s1, String s2) {
        i1.operation(s1, s2);
        i2.operation(s1, s2);
    }

    public static void main(String args[]) {
        OneMethodInterface v1 = (s1, s2) -> {
            System.out.println(s1);
            System.out.println(s2);
            return 0;
        };

        OneMethodInterface v2 = (s1, s2) -> {
            System.out.println(s2);
            System.out.println(s1);
            return 0;
        };

        v1.operation("a", "b");
        v2.operation("a", "b");
        
        System.out.println("---------");

        new MainClass().exec(v1, v2, "a", "b");

        return;
    }

}

