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
        editor.putString("refreshToken", data.getRefreshToken());
        editor.apply();
    }

    public UserData getCurrentUserData() {
        String refreshToken = "";
        refreshToken = sharedPreferences.getString("refreshToken", refreshToken);
        UserData data = UserData.getInstance();
        data.setRefreshToken(refreshToken);
        return data;
    }

    public void removeCurrentUserData(){
        SharedPreferences.Editor editor = sharedPreferences.edit();
        editor.remove("refreshToken");
        editor.apply();
    }
}
