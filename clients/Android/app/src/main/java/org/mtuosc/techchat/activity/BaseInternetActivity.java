package org.mtuosc.techchat.activity;

import android.support.v7.app.AppCompatActivity;
import android.widget.Toast;

import org.mtuosc.techchat.asynctasks.CheckConnectionTask;

import java.util.concurrent.ExecutionException;

abstract public class BaseInternetActivity extends AppCompatActivity {

    protected boolean hasInternet(){
        CheckConnectionTask checkConnectionTask = new CheckConnectionTask();
        checkConnectionTask.execute(getApplication());
        try {
            return checkConnectionTask.get();
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
        return false;
    }

    protected void showConnectionWarning(){
        Toast.makeText(this, "No Internet Connection", Toast.LENGTH_SHORT).show();
    }
}
