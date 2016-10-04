#![allow(dead_code)]

use std::io::{self, Read, Write};
use byteorder::{ByteOrder, NetworkEndian};

// FIXME: replace these with byteorder core io traits once those are in
pub fn read_u8(reader: &mut Read) -> io::Result<u8> {
    let mut bytes = [0; 1];
    try!(reader.read_exact(&mut bytes));
    Ok(bytes[0])
}

pub fn write_u8(writer: &mut Write, value: u8) -> io::Result<()> {
    let bytes = [value; 1];
    writer.write_all(&bytes)
}

pub fn read_u16(reader: &mut Read) -> io::Result<u16> {
    let mut bytes = [0; 2];
    try!(reader.read_exact(&mut bytes));
    Ok(NetworkEndian::read_u16(&bytes))
}

pub fn write_u16(writer: &mut Write, value: u16) -> io::Result<()> {
    let mut bytes = [0; 2];
    NetworkEndian::write_u16(&mut bytes, value);
    writer.write_all(&bytes)
}

pub fn read_u32(reader: &mut Read) -> io::Result<u32> {
    let mut bytes = [0; 4];
    try!(reader.read_exact(&mut bytes));
    Ok(NetworkEndian::read_u32(&bytes))
}

pub fn write_u32(writer: &mut Write, value: u32) -> io::Result<()> {
    let mut bytes = [0; 4];
    NetworkEndian::write_u32(&mut bytes, value);
    writer.write_all(&bytes)
}

pub fn read_u64(reader: &mut Read) -> io::Result<u64> {
    let mut bytes = [0; 8];
    try!(reader.read_exact(&mut bytes));
    Ok(NetworkEndian::read_u64(&bytes))
}

pub fn write_u64(writer: &mut Write, value: u64) -> io::Result<()> {
    let mut bytes = [0; 8];
    NetworkEndian::write_u64(&mut bytes, value);
    writer.write_all(&bytes)
}
