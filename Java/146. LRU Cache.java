class Node{
    int key;
    int val;
    Node prev;
    Node next;

    public Node(int key, int val){
        this.key = key;
        this.val=val;
        this.prev=null;
        this.next=null;
    }
}

class LRUCache {
    int cap;
    Map<Integer,Node> cache;
    Node oldest;
    Node latest;

    public LRUCache(int capacity) {
        this.cap = capacity;
        this.cache = new HashMap<>();
        this.oldest = new Node(0,0);
        this.latest = new Node(0,0);
        this.oldest.next = this.latest;
        this.latest.prev = this.oldest;
    }
    public void insert(Node node){
        Node prev= latest.prev;
        Node next = latest;
        prev.next = next.prev= node;
        node.prev = prev;
        node.next = next;
    }
    public void remove(Node node){
        Node prev= node.prev;
        Node next = node.next;
        prev.next = node.next;
        next.prev = node.prev;
    }
    public int get(int key) {
        if (cache.containsKey(key)){
            Node node = cache.get(key);
            remove(node);
            insert(node);
            return node.val;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if (cache.containsKey(key)){
            remove(cache.get(key));
        }
        Node newnode = new Node(key,value);
        cache.put(key,newnode);
        insert(newnode);

        if (cache.size()>cap){
            Node lru = oldest.next;
            remove(lru);
            cache.remove(lru.key);
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */