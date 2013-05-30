package com.example.tcp;



import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.MotionEvent;
import android.view.View;






public class welcome extends Activity {



	/** Called when the activity is first created. */
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.welcome_screen);
		}

	public boolean onTouchEvent(MotionEvent event){
	    int action = event.getAction();
	  

	    switch(action){
	    case MotionEvent.ACTION_DOWN:
	    	Intent intent=new Intent(welcome.this,main.class);      	
            startActivity(intent); 
	    	break;
	    
	    }
	    return true;
	}
	

	
	}