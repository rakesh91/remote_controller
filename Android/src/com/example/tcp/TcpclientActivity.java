package com.example.tcp;



import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import com.example.tcp.main;


import android.app.Activity;
import android.content.Intent;
import android.net.ParseException;
import android.os.Bundle;
import android.util.Log;
import android.view.MotionEvent;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

@SuppressWarnings("unused")
public class TcpclientActivity extends Activity {

	public static String TAG = "TcpClientActivity";

	int px=0,py=0,dx=0,dy=0,x=0,y=0;
	private EditText serverIP = null;
	private EditText serverPort = null;
	private EditText message = null;
	public Button keyboard=null;
	public Button left=null;
	public Button right=null;
	private TextView serverReplies = null;
	public Intent startNewActivityOpen;

	/** Called when the activity is first created. */
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.main);

		startNewActivityOpen = new Intent(TcpclientActivity.this, Keyboard.class);
    keyboard=(Button) findViewById(R.id.keyboard);
    left=(Button) findViewById(R.id.left);
    right=(Button) findViewById(R.id.right);
    
    keyboard.setOnClickListener(new View.OnClickListener() {
		
		@Override
		public void onClick(View v) {
			
			startActivityForResult(startNewActivityOpen, 0);
			
		}
	});
    
    left.setOnClickListener(new View.OnClickListener() {
		
		@Override
		public void onClick(View v) {
			click();
			
		}
	});
    
    
    right.setOnClickListener(new View.OnClickListener() {
		
		@Override
		public void onClick(View v) {
			Rightclick();
			
		}
	});
    
   
    
    
    
    		

	
	}
	
	public boolean onTouchEvent(MotionEvent event){
	    int action = event.getAction();
	  

	    switch(action){
	    case MotionEvent.ACTION_DOWN:
	    	 px = (int) event.getX();  // or getRawX();
	  	     py = (int) event.getY();
	    	break;
	    case MotionEvent.ACTION_MOVE:
	    	 x = (int) event.getX();  // or getRawX();
	  	     y = (int) event.getY();
	  	   dx=x-px;
	  	     dy=y-py;
	  	     px=x;
	  	     py=y;
	  	   Log.v(TAG, "TOuch");
	    	move(dx,dy);
	        break;
	    }
	    return true;
	}
	
	
	public void move(int x,int y)//function
	{
		
	
		try{
		
		 InetAddress serverAddr = InetAddress.getByName(main.ip.getText().toString());
         
         Log.d("UDP", "C: Connecting...");
         /* Create new UDP-Socket */
         DatagramSocket socket = new DatagramSocket();
        
         /* Prepare some data to be sent. */
         byte[] buf = ("M="+new Integer(x).toString()+"="+new Integer(y).toString()).getBytes();//message
        
         /* Create UDP-packet with
          * data & destination(url+port) */
         DatagramPacket packet = new DatagramPacket(buf, buf.length,     serverAddr, 5001);
         Log.d("UDP", "C: Sending: '" + new String(buf) + "'");
        
         /* Send out the packet */
         socket.send(packet);
         Log.d("UDP", "C: Sent.");
         Log.d("UDP", "C: Done.");
		

	} catch (Exception e) {
		serverReplies.setText(e.getMessage());
		Log.v(TAG, e.toString());
	} 
	}
	
	public void click()
	{
		try{
		 InetAddress serverAddr = InetAddress.getByName(main.ip.getText().toString());
         
         Log.d("UDP", "C: Connecting...");
         /* Create new UDP-Socket */
         DatagramSocket socket = new DatagramSocket();
        
         /* Prepare some data to be sent. */
         byte[] buf = ("C="+"1"+"="+"1").getBytes();
        
         /* Create UDP-packet with
          * data & destination(url+port) */
         DatagramPacket packet = new DatagramPacket(buf, buf.length,     serverAddr, 5001);
         Log.d("UDP", "C: Sending: '" + new String(buf) + "'");
        
         /* Send out the packet */
         socket.send(packet);
         Log.d("UDP", "C: Sent.");
         Log.d("UDP", "C: Done.");
		

	} catch (Exception e) {
		serverReplies.setText(e.getMessage());
		Log.v(TAG, e.toString());
	} 
	}
	
	
	public void Rightclick()
	{
		try{
		 InetAddress serverAddr = InetAddress.getByName(main.ip.getText().toString());
         
         Log.d("UDP", "C: Connecting...");
         /* Create new UDP-Socket */
         DatagramSocket socket = new DatagramSocket();
        
         /* Prepare some data to be sent. */
         byte[] buf = ("R="+"1"+"="+"1").getBytes();
        
         /* Create UDP-packet with
          * data & destination(url+port) */
         DatagramPacket packet = new DatagramPacket(buf, buf.length,     serverAddr, 5001);
         Log.d("UDP", "C: Sending: '" + new String(buf) + "'");
        
         /* Send out the packet */
         socket.send(packet);
         Log.d("UDP", "C: Sent.");
         Log.d("UDP", "C: Done.");
		

	} catch (Exception e) {
		serverReplies.setText(e.getMessage());
		Log.v(TAG, e.toString());
	} 
	}

	
	
	
}