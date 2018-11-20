package org.mtuosc.techchat.activity;

import android.support.v7.app.AppCompatActivity;
import android.widget.Toast;

import org.mtuosc.techchat.UserData;
import org.mtuosc.techchat.asynctasks.AsyncApiResponse;
import org.mtuosc.techchat.asynctasks.CheckConnectionTask;
import org.mtuosc.techchat.asynctasks.RefreshAccessToken;
import org.mtuosc.techchat.asynctasks.RefreshResponder;

import java.util.concurrent.ExecutionException;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;

abstract public class BaseInternetActivity extends AppCompatActivity {
    protected UserData user = UserData.getInstance();

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

    protected void refreshAccessToken(RefreshResponder responder) {
        if (!user.isAccessTokenValid()){
            RefreshAccessToken refreshAccessToken = new RefreshAccessToken(responder);
            refreshAccessToken.setRefreshToken(user.getRefreshToken());
            refreshAccessToken.execute();
        }
        responder.respondToRefresh(user.getAccessToken()); // access token good let caller know
    }
}
