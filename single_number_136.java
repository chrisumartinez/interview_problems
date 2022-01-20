public class single_number_136 {

    public int singleNumber(int[] nums) {
        int val = 0;
        for (int num : nums) {
            val ^= num;
        }
        return val;
    }

    public static void main(String[] args) {
        single_number_136 driver = new single_number_136();
        int[] nums = { 4, 1, 2, 1, 2 };
        System.out.println(driver.singleNumber(nums));
    }

}
