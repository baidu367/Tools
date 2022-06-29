package xxx;
import okhttp3.*;
import java.io.IOException;
//java程序发送请求

public class Demo {
    public static void main(String[] args) {
        long timestamp = System.currentTimeMillis()/1000;
        String arg = "*****";
        String url = "https://XXXX.XXXXX.XXXX/XXX";
        try {
            // 初始化 OkHttpClient
            OkHttpClient client = new OkHttpClient();
            //请求参数体
            RequestBody requestBody = new FormBody.Builder()
                    .add("page",String.valueOf(1))
                    //.add("sign",resp)
                    .add("t",String.valueOf(timestamp))
                    .build();
            // 初始化请求体
            Request request = new Request.Builder()
                    .post(requestBody)
                    .url(url)
                    .build();
            // 得到返回Response
            Response response = client.newCall(request).execute();
            System.out.println(response.body().string());
        }
        catch (IOException e) {
            e.printStackTrace();
        }

    }
}
