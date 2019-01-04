package org.mtuosc.techchat.activity;

import android.os.Bundle;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;

import org.mtuosc.techchat.R;

public class PostActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.post_activity_main);

        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        toolbar.setTitle("Posts for Board");
        setSupportActionBar(toolbar);
        ActionBar actionBar  =  getSupportActionBar();
        actionBar.setDisplayHomeAsUpEnabled(true);




    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.post_menu, menu);
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
