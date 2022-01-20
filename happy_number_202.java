public class happy_number_202 {

    public int squareSum(int n) {
        int total = 0;
        while (n > 0) {
            int digit = n % 10;
            total += digit * digit;
            n = n / 10;
        }
        return total;

    }

    public boolean isHappy(int n) {
        int slow = n;
        int fast = n;
        do {
            slow = squareSum(slow);
            fast = squareSum(squareSum(fast));

        } while (slow != fast);
        if (slow == 1) {
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        int number = 19;
        happy_number_202 driver = new happy_number_202();
        System.out.println(driver.isHappy(number));
    }

}