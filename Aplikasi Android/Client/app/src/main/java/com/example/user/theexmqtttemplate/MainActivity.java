package com.example.user.theexmqtttemplate;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallbackExtended;
import org.eclipse.paho.client.mqttv3.MqttMessage;

import mesin_iot.Helper_IoT;

public class MainActivity extends AppCompatActivity {

    EditText jumlah;
    Button beli;
    TextView stok;
    Helper_IoT helper_iot;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        stok = (TextView) findViewById(R.id.textView7);
        beli = (Button) findViewById(R.id.button);
        jumlah = (EditText) findViewById(R.id.editText);



        helper_iot = new Helper_IoT(getApplicationContext());
        helper_iot.setCallback(new MqttCallbackExtended() {
            @Override
            public void connectComplete(boolean reconnect, String serverURI) {

            }

            @Override
            public void connectionLost(Throwable cause) {

            }

            @Override
            public void messageArrived(String topic, MqttMessage message) throws Exception {
                String list_payload = stok.getText().toString();
                list_payload = ""+message;
                stok.setText(list_payload);
            }

            @Override
            public void deliveryComplete(IMqttDeliveryToken token) {

            }
        });

        beli.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String payload = jumlah.getText().toString();
                helper_iot.mqttPublish(payload);
                jumlah.setText(payload);
            }
        });


    }
}
