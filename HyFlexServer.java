import py4j.GatewayServer;

public class HyFlexServer {
    public static void main(String[] args) {
        GatewayServer gatewayServer = new GatewayServer();
        gatewayServer.start();
        System.out.println("HyFlex Server Started");
    }
}
