webpackJsonp(["save-page.module"],{

/***/ "./src/app/save-page/save-page-routing.module.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return SavePageRoutingModule; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("./node_modules/@angular/core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_router__ = __webpack_require__("./node_modules/@angular/router/esm5/router.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__app_core_services__ = __webpack_require__("./src/app/core/services/index.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__save_page_component__ = __webpack_require__("./src/app/save-page/save-page.component.ts");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};




var routes = [
    {
        path: '',
        component: __WEBPACK_IMPORTED_MODULE_3__save_page_component__["a" /* SavePageComponent */]
    },
    {
        path: 'explore-and-book/:project_id',
        canActivate: [__WEBPACK_IMPORTED_MODULE_2__app_core_services__["a" /* AuthGuardService */]],
        loadChildren: './explore-and-book-page/explore-and-book-page.module#ExploreAndBookPageModule'
    }
];
var SavePageRoutingModule = /** @class */ (function () {
    function SavePageRoutingModule() {
    }
    SavePageRoutingModule = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["K" /* NgModule */])({
            imports: [__WEBPACK_IMPORTED_MODULE_1__angular_router__["c" /* RouterModule */].forChild(routes)],
            exports: [__WEBPACK_IMPORTED_MODULE_1__angular_router__["c" /* RouterModule */]]
        })
    ], SavePageRoutingModule);
    return SavePageRoutingModule;
}());



/***/ }),

/***/ "./src/app/save-page/save-page.component.html":
/***/ (function(module, exports) {

module.exports = "<p>\n  save-page works!\n\n  <button mat-button mat-raised-button color=\"primary\" (click)=gotToExploreAndBook()>Explore and book page</button>\n</p>\n"

/***/ }),

/***/ "./src/app/save-page/save-page.component.scss":
/***/ (function(module, exports) {

module.exports = ""

/***/ }),

/***/ "./src/app/save-page/save-page.component.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return SavePageComponent; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("./node_modules/@angular/core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_router__ = __webpack_require__("./node_modules/@angular/router/esm5/router.js");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};


var SavePageComponent = /** @class */ (function () {
    function SavePageComponent(router) {
        this.router = router;
    }
    SavePageComponent.prototype.ngOnInit = function () {
    };
    SavePageComponent.prototype.gotToExploreAndBook = function () {
        this.router.navigate(['/save/explore-and-book', 'ProjectIdComesHere']);
    };
    SavePageComponent = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["n" /* Component */])({
            selector: 'app-save-page',
            template: __webpack_require__("./src/app/save-page/save-page.component.html"),
            styles: [__webpack_require__("./src/app/save-page/save-page.component.scss")]
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1__angular_router__["b" /* Router */]])
    ], SavePageComponent);
    return SavePageComponent;
}());



/***/ }),

/***/ "./src/app/save-page/save-page.module.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "SavePageModule", function() { return SavePageModule; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("./node_modules/@angular/core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_common__ = __webpack_require__("./node_modules/@angular/common/esm5/common.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__save_page_routing_module__ = __webpack_require__("./src/app/save-page/save-page-routing.module.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__save_page_component__ = __webpack_require__("./src/app/save-page/save-page.component.ts");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};




var SavePageModule = /** @class */ (function () {
    function SavePageModule() {
    }
    SavePageModule = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["K" /* NgModule */])({
            imports: [
                __WEBPACK_IMPORTED_MODULE_1__angular_common__["b" /* CommonModule */],
                __WEBPACK_IMPORTED_MODULE_2__save_page_routing_module__["a" /* SavePageRoutingModule */]
            ],
            declarations: [__WEBPACK_IMPORTED_MODULE_3__save_page_component__["a" /* SavePageComponent */]]
        })
    ], SavePageModule);
    return SavePageModule;
}());



/***/ })

});
//# sourceMappingURL=save-page.module.chunk.js.map