package com.example.steer_the_wheel;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.widget.TextView;

public class MainActivity extends Activity implements SensorEventListener {


    int accelXValue;
    int accelYValue;
    int accelZValue;

    int gyroX;
    int gyroY;
    int gyroZ;

    private SensorManager mSensorManager;
    private Sensor mGyroscope;
    private Sensor accSensor;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //센서 매니저 얻기
        mSensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        //자이로스코프 센서(회전)
        mGyroscope = mSensorManager.getDefaultSensor(Sensor.TYPE_GYROSCOPE);
        //엑셀러로미터 센서(가속)
        accSensor = mSensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);


    }
    //정확도에 대한 메소드 호출 (사용안함)
    public void onAccuracyChanged(Sensor sensor, int accuracy) {

    }


    //센서값 얻어오기
    public void onSensorChanged(SensorEvent event) {
        Sensor sensor = event.sensor;
        TextView textView1 = (TextView) findViewById(R.id.angleX) ;
        TextView textView2 = (TextView) findViewById(R.id.angleY) ;
        TextView textView3 = (TextView) findViewById(R.id.angleZ) ;
        if (sensor.getType() == Sensor.TYPE_GYROSCOPE) {
            gyroX = Math.round(event.values[0] * 1000);
            gyroY = Math.round(event.values[1] * 1000);
            gyroZ = Math.round(event.values[2] * 1000);
            //System.out.println("gyroX ="+gyroX);
            //System.out.println("gyroY ="+gyroY);
            //System.out.println("gyroZ ="+gyroZ);



        }
        if (event.sensor.getType() == Sensor.TYPE_ACCELEROMETER)
            accelXValue = (int) event.values[0];
        accelYValue = (int) event.values[1];
        accelZValue = (int) event.values[2];
        //System.out.println("accelXValue="+accelXValue);
        //System.out.println("accelYValue="+accelYValue);
        //System.out.println("accelZValue="+accelZValue);
        textView1.setText("Angle X : "+accelXValue) ;

        textView2.setText("Angle Y : "+accelYValue) ;

        textView3.setText("Angle Z : "+accelZValue) ;
    }

    // 주기 설명
    // SENSOR_DELAY_UI 갱신에 필요한 정도 주기
    // SENSOR_DELAY_NORMAL 화면 방향 전환 등의 일상적인  주기
    // SENSOR_DELAY_GAME 게임에 적합한 주기
    // SENSOR_DELAY_FASTEST 최대한의 빠른 주기


    //리스너 등록
    protected void onResume() {
        super.onResume();
        mSensorManager.registerListener(this, mGyroscope,SensorManager.SENSOR_DELAY_FASTEST);
        mSensorManager.registerListener(this, accSensor,SensorManager.SENSOR_DELAY_FASTEST);
    }

    //리스너 해제
    protected void onPause() {
        super.onPause();
        mSensorManager.unregisterListener(this);
    }
}
