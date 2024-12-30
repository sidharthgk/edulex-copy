<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::middleware(['auth:api'])->get('/user', function (Request $request) {
    return $request->user()->load('wallet');
});

// ping route
Route::get('/ping', function () {
    return response()->json(['message' => 'pong']);
});


require __DIR__.'/auth.php';
