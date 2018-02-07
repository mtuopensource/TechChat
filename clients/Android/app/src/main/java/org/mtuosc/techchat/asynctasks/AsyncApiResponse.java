package org.mtuosc.techchat.asynctasks;

/**
 * Created by ryan on 2/4/18.
 *  Use this interface when your activity uses an async task
 *  and relies on a return value
 */

public interface AsyncApiResponse<R> {

    void taskCompleted(R result);
}
