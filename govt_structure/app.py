import mainapp

app = mainapp.create_app()

#add host as 0.0.0.0 to be accessible from outside when running as a container
if __name__ == "__main__":
    app.run(host='0.0.0.0')