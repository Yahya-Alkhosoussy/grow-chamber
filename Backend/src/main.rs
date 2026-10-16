use amiquip::{Connection, Exchange, Publish, Result};
use std::fs::File;
use std::io::Read;

fn main() -> Result<()> {
    // Open connection.
    let mut connection = Connection::insecure_open("amqp://admin:secure_password@rabbitmq:5672")?;

    // Open a channel - None says let the library choose the channel ID.
    let channel = connection.open_channel(None)?;

    // Get a handle to the direct exchange on our channel.
    let exchange = Exchange::direct(&channel);

    let mut file = File::open("./images/image.jpg")
        .unwrap();

    let mut buffer = Vec::new();

    file.read_to_end(&mut buffer).unwrap();
        
    println!("Sending Image...");

    let first_few = &buffer.as_slice()[..3];

    println!("{:#?}", first_few);
    
    exchange.publish(Publish::new(buffer.as_slice(), "images"))?;
    
    // Publish a message to the "hello" queue.

    connection.close()
}