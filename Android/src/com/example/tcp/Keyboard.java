package com.example.tcp;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;


import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.Log;
import android.view.Menu;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class Keyboard extends Activity {

	public Button mouse=null;
	public Intent startNewActivityOpen;
	public EditText data=null;
	public TextView indicator=null;
	private TextView serverReplies = null;
	public static String TAG = "TcpClientActivity";
	public int oldlength;
	public int newlength;
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_keyboard);
		startNewActivityOpen = new Intent(Keyboard.this,TcpclientActivity.class);
		data=(EditText) findViewById(R.id.data);
		
		oldlength=0;
		newlength=0;
		mouse=(Button) findViewById(R.id.mouse);
		mouse.setOnClickListener(new View.OnClickListener() {
		
			@Override
			public void onClick(View v) {
				
				startActivityForResult(startNewActivityOpen, 0);
				
			}
		});
		
		data.addTextChangedListener(new TextWatcher() {
			
			@Override
			public void onTextChanged(CharSequence s, int start, int before, int count) {
				
				
				
			}
			
			@Override
			public void beforeTextChanged(CharSequence s, int start, int count,
					int after) {
				
				
			}
			
			@Override
			public void afterTextChanged(Editable s) {
				newlength=s.length();
				if(oldlength<=newlength)
				{
					
				
				for (int i = 0; i < s.subSequence(oldlength, newlength).length(); i++) {
		SendCharacter("1="+s.subSequence(oldlength, newlength).toString());
	
				}
				}
				else{
					SendCharacter("0=BackSpace");
				}
				
				oldlength=s.length();
			}
		});
		
		
	
		
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.activity_keyboard, menu);
		return true;
	}

	public void SendCharacter(String S)
	{
		
		try{
		 InetAddress serverAddr = InetAddress.getByName(main.ip.getText().toString());
         
         Log.d("UDP", "C: Connecting...");
         /* Create new UDP-Socket */
         DatagramSocket socket = new DatagramSocket();
        
         /* Prepare some data to be sent. */
         byte[] buf = ("K="+S).getBytes();
        
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
