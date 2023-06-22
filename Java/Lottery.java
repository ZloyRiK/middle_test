

import java.util.ArrayList;
import java.util.Random;

import Java.Toy;
import Java.storage.ToyStorage;

public class Lottery {
    private String participant;

    // Для каждого участника бузет вызываться конструктор и создаваться объект класса
    public Lottery(String participant){
        this.participant = participant;
    }

    ToyStorage ts = new ToyStorage();
    ArrayList <Toy> toys = ts.getAllToys();


    public String getPrize(){
        int sum = 0;
        Random random = new Random();
        int rnd = random.nextInt(100);
        String prize = "";
        int lastwinner=0;
        int[] chance = new int[toys.size()];
        
        for (int i = 0; i < chance.length; i++) {
            sum += toys.get(i).getQuantity();
        }

        for (int i = 0; i < chance.length; i++) {
            chance[i] = toys.get(i).getQuantity()/sum*100;
        }

        for (int i = 0; i < chance.length; i++) {
            if (chance[i]>lastwinner && chance[i]<=rnd){
                prize = toys.get(i).getName();
            }
        }
        System.out.println("Приз определен. Можете обратиться за выигрышем");
        return prize;
    }

    public String getParticipant(){
        return participant;
    }

}
