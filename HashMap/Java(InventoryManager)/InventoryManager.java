import java.util.HashMap;
import java.util.Map;

public class InventoryManager {
    private final Map<String, Integer> stockMap = new HashMap<>();

    public void addStock(String productId, int quantity) {
        stockMap.merge(productId, quantity, Integer::sum);
    }

    public void removeStock(String productId, int quantity) {
        stockMap.computeIfPresent(productId, (id, current) ->
                Math.max(0, current - quantity));
    }

    public int checkStock(String productId) {
        return stockMap.getOrDefault(productId, 0);
    }

    public void printInventory() {
        stockMap.forEach((id, qty) ->
                System.out.printf("Product %s: %d units%n", id, qty));
    }
}