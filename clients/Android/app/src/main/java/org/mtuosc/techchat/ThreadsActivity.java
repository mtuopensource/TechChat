package org.mtuosc.techchat;

import android.content.Intent;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        final Intent changeActivity = new Intent(this, Main2Activity.class);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(changeActivity);
            }
        });
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        menu.getItem(0).getSubMenu().getItem(0).setChecked(true); // this grabs the recent menu option

        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();
        switch (id){
            // TODO replace the duplicate code with function / classes
            case R.id.menu_sort_recent:
                if (! item.isChecked()) {
                    // call the sort function
                    item.setChecked(true);
                }
                break;
            case R.id.menu_sort_oldest:
                if (! item.isChecked()) {
                    // call the sort function
                    item.setChecked(true);
                }
                break;
            case R.id.menu_sort_trending:
                if (! item.isChecked()) {
                    // call the sort function
                    item.setChecked(true);
                }
                break;
        }

        return super.onOptionsItemSelected(item);
    }
}
