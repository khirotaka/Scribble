use std::sync::{mpsc, Arc, Mutex};
use std::thread;


fn main() {
    let (sender, reciver) = mpsc::channel();
    let rx = Arc::new(Mutex::new(reciver));
    let mut threads = Vec::new();

    for i in 0..5 {
        let rx = Arc::clone(&rx);
        let th = thread::spawn(move ||{
            let rx = rx.lock().unwrap();
            println!("thread {} - receiver: {}", i, rx.recv().unwrap());
        });

        threads.push(th);
    }

    for i in 0..5 {
        sender.send(i).unwrap();
    }

    for t in threads {
        t.join().unwrap();
    }
}
