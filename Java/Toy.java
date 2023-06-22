package Java;

public class Toy implements Comparable<Toy>{
    private static int count = 0;
    private int id;
    private String name;
    private int quantity;

    public Toy(String name, int quantity) {
        this.name = name;
        this.quantity = quantity;
        count++;
        this.id = getCount();
    }

    public static int getCount(){
        return count;
    }

    public int getId(){
        return id;
    }

    public String getName(){
        return name;
    }

    public int getQuantity(){
        return quantity;
    }
    public void setQuantity(int quantity){
        this.quantity = quantity;
    }

    @Override
    public int compareTo(Toy t){
        return Integer.compare(this.id, t.getId());
    }
}
