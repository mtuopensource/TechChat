package org.mtuosc.techchat;


import android.content.SharedPreferences;


/**
 * Writes and retrieves User data from shared preference files
 * Note: only one user can be saved at a time
 */
public class UserDataStorage {

    private SharedPreferences sharedPreferences;


    public UserDataStorage(SharedPreferences preferencesFile) {
        sharedPreferences = preferencesFile;
    }

    public void saveUserData(UserData data) {
        SharedPreferences.Editor editor = sharedPreferences.edit();
        editor.putString("cookie", data.getCookie());
        editor.apply();
    }

    public UserData getCurrentUserData() {
        String cookie = "";
        cookie = sharedPreferences.getString("cookie", cookie);
        return new UserData(cookie);
    }
}
