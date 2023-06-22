package Java;

public class MainTest {
    public static void main(String[] args) {
        
        Toy t1 = new Toy("Toy1", 5);
        System.out.printf("count: %d    id: %d\n",Toy.getCount(), t1.getId());

        Toy t2 = new Toy("Toy2", 8);
        System.out.printf("count: %d    id: %d\n",Toy.getCount(), t2.getId());

        Toy t3 = new Toy("Toy3", 7);
        System.out.printf("count: %d    id: %d\n",Toy.getCount(), t3.getId());

        Toy t4 = new Toy("Toy4",3);
        System.out.printf("count: %d    id: %d\n",Toy.getCount(), t4.getId());
    }
}
