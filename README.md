This guide is intended to address frustrations one may bump into while trying to figure out how to build Spotify's models. It is also written in a way for which individuals with lesser technical experience can navigate through and build the models themselves. I've also included a few scripts to help expedite some processes.

Firstly, I must say that a good portion of the instructions and this workspace itself was curated by Brian Lach. You can find his Github [here](https://github.com/lachbr).

Additionally, I must add that these are instructions for Windows only.

# Required files
- You need to have [this](https://github.com/loonaticx/ttmodels) modified version of Spotify cloned anywhere on your computer. This is the workspace we will be using.

- You need to be able to use the program [``make``](https://chocolatey.org/packages/make) to build the models. You can check whether or not you have make already installed by typing it in the command prompt. If you do not have make installed, I would install [Chocolatey:](https://chocolatey.org/install)
  - With Chocolatey, you can install make via ``choco install make`` in the command line or Powershell.

- Lastly, I highly recommend (although not officially required) using a build of Panda3D with [this](https://github.com/panda3d/panda3d/commit/74a464896589f2ae0fa0c9f3b1728abc9fd9182f) commit. This reintroduces the maya2egg server, which would greatly reduce the total time it will take to build all of the models.
  - If you do not already have a Panda3D install with Maya support, you will need to either build or install a version with the Maya tools.

# Configuring ppremake

Panda Premake ("ppremake") is a deprecated tool that was originally used to build and convert files en masse for the Panda3D engine. While the binary is no longer available in modern versions of Panda, it was built to be compatible as a standalone application. To save time and possible frustration, I've included a prebuilt version of ppremake located within the ttmodels directory.

If you decide not to use a Panda3D version with Maya support, you must open [**ttmodels/Package.pp**](https://github.com/tsp-team/ttmodels/blob/master/ttmodels/Package.pp) and change the line reading `#define MAYA2EGG maya2egg_client` to `#define MAYA2EGG maya2egg<MAYAVERSION>`. *Note that `<MAYAVERSION>` should be replaced with the version of Maya you are using along with the version of maya2egg your Panda3D installation comes with.*

If you are using a Panda3D build with Maya server support, ensure that you have the Maya service running in the background *before starting the build process*. Simply open up a new command prompt and run ``maya2egg<MAYAVERSION> -server``. Any time you would like to convert a Maya file to an Egg file, you would simply run ``maya2egg_client <input.mb> <output.egg>`` on a new shell instance.

## Notice

Due to a bug within **char/boss/Sources.pp**, you will need to adjust the line reading ``#define MAYA2EGG maya2egg`` to ``#define MAYA2EGG maya2egg<MAYAVERSION>``. If you are using a maya2egg server, do **NOT** use the client version (``maya2egg_client``). Instead, use the same maya2egg version as the server you're hosting.

This means that all of the models within **char/boss/** will have to be converted in a manual fashion, which will briefly slow down the build process.

# Generating Makefiles

Once adjusting our build configurations, we will let ppremake scrub over all the Sources.pp files within the model tree to generate Makefiles that will build the assets.

In order to do this, we can simply call ``ppremake.exe`` while inside our ttmodels folder.

## Rebuilding Makefiles

If any adjustments are made to a Panda premake file, you **must** delete all instances of "Makefile" within all the child directories and re-run ppremake. I've included several scripts to help expedite this process.

# Building Models

After generating makefiles and building the model tree, we are ready to build our models. **Keep in mind this may take a long time, possibly several hours, to complete building.**

In the ttmodels directory, run ``make install`` inside your command prompt.

# Debugging Errors

While building the models, make may run into an error and stop building. Here are some solutions to common issues:

### Error
```
make[1]: Entering directory '...ttmodels/char/boss'
maya2egg -uo ft -tbnall -nv 60 -TS 0.12 -o bossCog-gearCollide.egg bossCog-gearCollide.mb
process_begin: CreateProcess(NULL, maya2egg -uo ft -tbnall -nv 60 -TS 0.12 -o bossCog-gearCollide.egg bossCog-gearCollide.mb, ...) failed.
make (e=2): The system cannot find the file specified.
make[1]: *** [Makefile:331: bossCog-gearCollide.egg] Error 2
make[1]: Leaving directory '...ttmodels/char/boss'
make: *** [Makefile:828: egg-boss] Error 2
```

### Solution
Refer to the **"Configuring ppremake"** section of this document.

### Error
```
make[1]: Entering directory '...ttmodels/char/boss'
maya2egg_client -uo ft -tbnall -nv 60 -TS 0.12 -a chan -cn "bossCog-head" -o bossCog-head-Bf_neutral.egg -sf 1 -ef 72 SB_Bf_neutral.mb
No response has been given by the conversion server.
make[1]: *** [Makefile:481: bossCog-head-Bf_neutral.egg] Error 1
```

### Solution
Refer to **"Configuring ppremake"** of this document and read the notice section. 
