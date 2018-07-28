package org.mtuosc.techchat.asynctasks;

import android.content.Context;

import android.os.AsyncTask;

import org.mtuosc.techchat.ApiUrl;


import java.net.InetAddress;

public class CheckConnectionTask extends AsyncTask<Context, Void, Boolean> {

    @Override
    protected Boolean doInBackground(Context... voids) {
        try {
            InetAddress ipAddr = InetAddress.getByName(ApiUrl.SERVER_HOSTNAME);
            //You can replace it with your name
            return !ipAddr.equals("");

        } catch (Exception e) {
            return false;
        }
    }
}
