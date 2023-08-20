use std::sync::mpsc;
use std::thread;

fn main() {
    let (sender, revicer) = mpsc::channel();

    thread::spawn(move ||{
        let val = String::from("World!");
        sender.send(val).unwrap();
    });

    let reviced = revicer.recv().unwrap();
    println!("Hello, {}", reviced);
}
