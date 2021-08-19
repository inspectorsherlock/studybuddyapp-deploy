package org.postgresql.test.jdbc3;

import org.postgresql.test.jdbc2.BaseTest4;

import org.junit.Test;

import java.sql.SQLException;
import java.sql.Statement;

public class TestCommitError extends BaseTest4 {

  @Test
  public void testCommitError() throws SQLException {
    Statement stmt = con.createStatement();

    con.setAutoCommit(false);
    try {
      stmt.executeQuery("select * from sometablethatdoesnotexist");
    } catch (Exception ex ) {
      // ignore it
    }

    try {
      con.commit();
    } catch (Exception ex ){
      System.err.printf("exception thrown %s\n", ex.getMessage());
      System.exit(0);
    }
    System.err.println("Should not get here");


  }
}
