use std::io::BufReader;
use std::io::prelude::*;
use std::fs::File;

fn main() -> std::io::Result<()>
{

    let file = File::open("simple_input.txt")?;     //if there is a error, it will send back cause ?
    let mut reader = BufReader::new(file);
    let mut line = String::new();
    reader.read_to_string(&mut line)?;

    let mut i = 0;
    let mut max = 0;

    if line != "\n" {
        let num = line.parse::<i32>().unwrap();
        i += num;
    }
    else{
        if max < i{
            max = i;
        }
        i = 0;
    }

    //TODO: if line == "\n"
    //TODO: añadir variable local suma
    //TODO: array de valores


    //TODO: devolver el maximo valor del array

    println!("{}", max);
    Ok(())
}