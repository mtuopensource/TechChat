package org.mtuosc.techchat;


import android.content.SharedPreferences;


import java.util.HashMap;


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
        editor.putString("useranme", data.getUsername());
        editor.putString("password", data.getPassword());
        editor.apply();
    }

    public UserData getCurrentUserData() {
        HashMap<String, String> dataItem = new HashMap<>();
        String[] dataItemKeys = {"refreshToken", "username", "password"};
        for (String item: dataItemKeys) {
            String value = "";
            value = sharedPreferences.getString(item, value);
            dataItem.put(item, value);
        }
        UserData data = UserData.getInstance();
        data.setRefreshToken(dataItem.get("refreshToken"));
        data.setPassword(dataItem.get("password"));
        data.setUsername(dataItem.get("username"));
        return data;
    }

    public void removeCurrentUserData(){
        SharedPreferences.Editor editor = sharedPreferences.edit();
        editor.remove("refreshToken");
        editor.apply();
    }
}
