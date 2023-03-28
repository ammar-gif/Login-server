FROM openjdk:19-jdk
ARG MAVEN_VERSION=3.6.3
EXPOSE 8082
COPY pom.xml /Users-server
ADD target/spring-boot-docker.jar spring-boot-docker.jar
ENTRYPOINT ["java","-jar","/spring-boot-docker.jar"]