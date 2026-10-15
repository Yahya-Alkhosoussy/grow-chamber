use amiquip::{Connection, Exchange, Publish, Result};
use image::ImageReader;



fn main() -> Result<()> {
    // Open connection.
    let mut connection = Connection::insecure_open("amqp://admin:secure_password@rabbitmq:5672")?;

    // Open a channel - None says let the library choose the channel ID.
    let channel = connection.open_channel(None)?;

    // Get a handle to the direct exchange on our channel.
    let exchange = Exchange::direct(&channel);

    let contents = ImageReader::open("./images/image.jpg")
        .unwrap()
        .decode()
        .unwrap();
        
    println!("Sending Image...");
    
    exchange.publish(Publish::new(contents.as_bytes(), "images"))?;
    
    // Publish a message to the "hello" queue.

    connection.close()
}