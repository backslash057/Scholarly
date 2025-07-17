package com.backslash057.scholarly

import android.content.Intent
import android.os.Bundle
import com.google.android.material.bottomnavigation.BottomNavigationView
import androidx.appcompat.app.AppCompatActivity
import androidx.navigation.findNavController
import androidx.navigation.ui.AppBarConfiguration
import androidx.navigation.ui.setupActionBarWithNavController
import androidx.navigation.ui.setupWithNavController
import com.backslash057.scholarly.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

//        val prefs = getSharedPreferences("auth", MODE_PRIVATE)
//        val token = prefs.getString("jwt", null)
//
//        if (token == null) {
//            startActivity(Intent(this, LoginActivity::class.java))
//            finish()
//            return
//        }
//        else {
//
//        }

        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val navView: BottomNavigationView = binding.navView

        val navController = findNavController(R.id.nav_host_fragment_activity_main)
        // Passing each menu ID as a set of Ids because each
        // menu should be considered as top level destinations.
        val appBarConfiguration = AppBarConfiguration(
            setOf(
                R.id.navigation_home, R.id.navigation_chat,
                R.id.navigation_note, R.id.navigation_finance
            )
        )

        navView.setupWithNavController(navController)
    }
}