package Java.storage;

import java.util.ArrayList;
import java.util.Collections;

import Java.Toy;

public class ToyStorage {
        
    private ArrayList <Toy> storageList = new ArrayList<Toy>();

    public void saveToy(Toy toy){
        storageList.add(toy);
        Collections.sort(storageList);
    }


    public ArrayList<Toy> getAllToys(){
        return storageList;
    }

    public Toy getToy(int id){
        return storageList.get(id);
    }

}
