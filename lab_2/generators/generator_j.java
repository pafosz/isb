package generators;
import java.util.Random;

public class generator_j {
    public static int random_generator(){
        Random random = new Random();
        return random.nextInt(2);   
    }

    public static void random_sequece(int num_bits){
        for(int i = 0; i < num_bits; i++){
            System.out.print(random_generator());
        }
        System.out.println();
    }
    public static void main(String[] args) {
        final int NUMBER_BITS = 128;
        random_sequece(NUMBER_BITS);
    }
}