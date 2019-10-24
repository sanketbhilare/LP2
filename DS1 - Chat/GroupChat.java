import java.util.*;
import java.io.*;
import java.net.*;

public class GroupChat {
	private static final String END = "exit";
	static String name;
	static volatile boolean finish = false;
	public static void main(String[] args){
		if(args.length != 2){
			System.out.println("Error: IP/PORT not mentioned\njava GroupChat <multi-cast IP> <PORT>");
		}
		else{
			try{
				Scanner in = new Scanner(System.in);
				InetAddress group = InetAddress.getByName(args[0]);
				int port = Integer.parseInt(args[1]);
				System.out.println("Enter Name: ");
				name = in.nextLine();
				MulticastSocket socket = new MulticastSocket(port);
				socket.joinGroup(group);
				Thread t = new Thread(new ReadThread(socket,group,port));
				t.start();
				System.out.println("Type: ");
				while(true){
					String message;
					message = in.nextLine();
					if(message.equalsIgnoreCase(END)){
						message = name + ": BYE...";
						byte[] buffer;
						buffer = message.getBytes();
						DatagramPacket datagram = new DatagramPacket(buffer, buffer.length,group,port);
						socket.send(datagram);
						finish = true;
						socket.leaveGroup(group);
						socket.close();
						break;
					}
					else{
						message = name + ": " + message;
						System.out.println(message);
						byte[] buffer;
						buffer = message.getBytes();
						DatagramPacket datagram = new DatagramPacket(buffer, buffer.length,group,port);
						socket.send(datagram);
					}
				}
			}
			catch(SocketException se){
				System.out.println("Error");
				se.printStackTrace();
			}
			catch(IOException ie){
				System.out.println("Error");
				ie.printStackTrace();
			}
		}
	}
}

class ReadThread implements Runnable{
	private MulticastSocket socket;
	private InetAddress group;
	private int port;
	private static final int MAX_LEN = 1000;
	ReadThread(MulticastSocket socket, InetAddress group, int port) {
		this.socket = socket;
		this.group = group;
		this.port = port;
	}
	public void run(){
		while(!GroupChat.finish){
			byte[] buffer = new byte[ReadThread.MAX_LEN];
			DatagramPacket datagram = new DatagramPacket(buffer, buffer.length,group,port);
			String message;
			try{
				socket.receive(datagram);
				message = new String(buffer,0,datagram.getLength(),"UTF-8");
				if(!message.startsWith(GroupChat.name)){
					System.out.println(message+"\nType: ");
				}
			}
			catch(IOException ie){
				System.out.println("Error");
				ie.printStackTrace();
			}
		}
	}
}

