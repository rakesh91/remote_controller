package com.example.tcp;



import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;





public class main extends Activity {

	public static Button next;
	public static EditText ip;

	/** Called when the activity is first created. */
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.mainscreen);
		
		 next=(Button) findViewById(R.id.button1);
		 ip=(EditText)findViewById(R.id.editText1);

		next.setOnClickListener(new View.OnClickListener() {
			
			public void onClick(View v) {
				// TODO Auto-generated method stub
				Intent intent=new Intent(main.this,TcpclientActivity.class);      	
                startActivity(intent); 
			}
		});
	

	
	}
	

	
	
}