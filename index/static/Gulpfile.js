var gulp 	   			= require('gulp');
var gulp_browserify  	= require('gulp-browserify');
var gulp_stripDebug 	= require('gulp-strip-debug');
var gulp_plumber    	= require('gulp-plumber');
var gulp_uglify	    	= require('gulp-uglify');
var gulp_watch     		= require('gulp-watch');

var browserify      	= require('browserify');
var babelify   			= require('babelify');
var buffer     			= require('vinyl-buffer');
var source     			= require('vinyl-source-stream');


gulp.task('js', function () {
	var jsSrc = "./javascriptsdev/main.js";
	var jsDst = "./javascripts/";
 	gulp.src(jsSrc)
    .pipe(gulp_browserify())
    .pipe(gulp_stripDebug(jsSrc))
    .pipe(gulp.dest(jsDst))
});

gulp.task('es6Toes5', function () {
	var jsSrc = "./javascriptsdev/main.js";
	var jsDst = "./javascripts/";
 	return browserify({
					    entries: (jsSrc),
					    debug: true
					  }).transform("babelify", { presets: ["es2015"], sourceMapsAbsolute: true})
 						.bundle()
					    .pipe(source('main.js'))
					    .pipe(buffer())
					    .pipe(gulp_uglify())
					    .pipe(gulp.dest(jsDst));
});

gulp.task('watch', function(){
  gulp.watch('./app/javascripts/backbone/main.js', ['es6Toes5']);
});

gulp.task('watch-js', function(){
  gulp.watch('./app/javascripts/backbone/main.js', ['js']);
});


gulp.task('default', ['watch']);