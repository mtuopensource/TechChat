package org.mtuosc.techchat.utils;

import org.junit.Test;

import static org.junit.Assert.*;

public class EmailPasswordValidatorTest {
    private EmailPasswordValidator validator = new EmailPasswordValidator();

    @Test
    public void badEmail(){
        String badEmail = "ksjdlfjsldjf";
        assertFalse(validator.isEmailValid(badEmail));
    }

    @Test
    public void goodEmail(){
        String goodEmail = "test@mtu.edu";
        assertTrue(validator.isEmailValid(goodEmail));
    }

    @Test
    public void badPassword(){
        String badPassword = "";
        assertFalse(validator.isPasswordValid(badPassword));
    }

    @Test
    public void goodPassword(){
        String goodPassword = "slkdjflskjdf";
        assertTrue(validator.isPasswordValid(goodPassword));
    }


}