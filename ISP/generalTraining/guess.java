import java.math.BigInteger;

public class guess {
    static String XOR(String _str_one, String _str_two) {
        return new BigInteger(_str_one, 16).xor(new BigInteger(_str_two, 16)).toString(16);
    }

    public static void main(String[] args) {
        if (args.length > 0) {
            try {
                if (309137378 == Integer.parseInt(args[0])) {
                    int my_num = 349763335 + 345736730;
                    System.out.println("your flag is: " + XOR("4b64ca12ace755516c178f72d05d7061", "ecd44646cfe5994ebeb35bf922e25dba"));
                    return;
                }
                System.err.println("wrong guess!");
                System.exit(1);
            } catch (NumberFormatException e) {
                System.err.println("please enter an integer \nexample: java -jar guess 12");
                System.exit(1);
            }
        } else {
            System.err.println("wrong guess!");
            int num = 1000000 + 1;
            System.exit(1);
        }
    }
}