# Print In Order - Synchronized

Suppose we have a class:

```java
public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
```

The same instance of `Foo` will be passed to three different threads. Thread A will call `first()`, thread B will call `second()`, and thread C will call `third()`. Design a mechanism and modify the program to ensure that `second()` is executed after `first()`, and `third()` is executed after `second()`.

```
Input: nums = [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output
```

## Intuition

[Explain your initial approach and thought process]

## Approach

[Detailed steps of your solution strategy]

1. a
    - b
2. c
    - d
        - e

## Complexity

- Time complexity: O(?)
- Space complexity: O(?)

## Code

<details>

<summary>Java - AtomicInteger and Synchronized</summary>

```java
class Foo {

    private final AtomicInteger i = new AtomicInteger();
    private final Object lock = new Object();

    public Foo() {
        i.set(0);
    }

    public void first(Runnable printFirst) throws InterruptedException {
        synchronized (lock){
            while (i.get() != 0){
                lock.wait();
            }
            printFirst.run();
            i.set(1);
            lock.notifyAll();
        }
    }

    public void second(Runnable printSecond) throws InterruptedException {
        
        synchronized (lock){
            while (i.get() != 1){
                lock.wait();
            }
            printSecond.run();
            i.set(2);
            lock.notifyAll();
        }
    }

    public void third(Runnable printThird) throws InterruptedException {
        synchronized(lock) {
            while (i.get() != 2){
                lock.wait();
            }
        }
        printThird.run();
        i.set(3);
    }
}
```
</details>

<details>

<summary>Python - Thread Locking</summary>

```python
from threading import Lock

class Foo:
    def __init__(self):
        self.firstJobDone = Lock()
        self.secondJobDone = Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first".
        printFirst()
        # Notify the thread that is waiting for the first job to be done.
        self.firstJobDone.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # Wait for the first job to be done
        with self.firstJobDone:
            # printSecond() outputs "second".
            printSecond()
            # Notify the thread that is waiting for the second job to be done.
            self.secondJobDone.release()

    def third(self, printThird: 'Callable[[], None]') -> None:

        # Wait for the second job to be done.
        with self.secondJobDone:
            # printThird() outputs "third".
            printThird()
```
</details>

## Notes

[Any additional notes or alternative approaches]
