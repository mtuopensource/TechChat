package org.mtuosc.techchat.utils;
import org.mtuosc.techchat.BuildConfig;

public class Version {
    private static int codeVersion = BuildConfig.VERSION_CODE;
    private static String versionName = BuildConfig.VERSION_NAME;

    public static String getAppVersion() { return versionName;}


    public static String prettyVersionNumber() {
        return "TechChat code version: " + String.valueOf(codeVersion) + "\n" +
                "TechChat version: " + versionName + "\n";
    }


}
