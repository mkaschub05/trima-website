// Usage: sharpen <in> <out.png> <x> <y> <w> <h> <targetWidth> <unsharpRadius> <unsharpIntensity> [brightness contrast]
// Crop (top-left origin), scale with Lanczos, then unsharp mask. Writes PNG.
import Foundation
import CoreImage
import CoreImage.CIFilterBuiltins
import ImageIO
import UniformTypeIdentifiers

let a = CommandLine.arguments
let input = CIImage(contentsOf: URL(fileURLWithPath: a[1]))!
let (x, y, w, h) = (Double(a[3])!, Double(a[4])!, Double(a[5])!, Double(a[6])!)
let targetW = Double(a[7])!
let H = input.extent.height
var img = input.cropped(to: CGRect(x: x, y: H - y - h, width: w, height: h))
img = img.transformed(by: CGAffineTransform(translationX: -x, y: -(H - y - h)))

let scale = CIFilter.lanczosScaleTransform()
scale.inputImage = img
scale.scale = Float(targetW / w)
scale.aspectRatio = 1
img = scale.outputImage!

let sharp = CIFilter.unsharpMask()
sharp.inputImage = img
sharp.radius = Float(a[8])!
sharp.intensity = Float(a[9])!
img = sharp.outputImage!.cropped(to: img.extent)
if a.count > 11 {
    let cc = CIFilter.colorControls()
    cc.inputImage = img
    cc.brightness = Float(a[10])!
    cc.contrast = Float(a[11])!
    cc.saturation = 1.05
    img = cc.outputImage!.cropped(to: img.extent)
}

let ctx = CIContext()
let cg = ctx.createCGImage(img, from: img.extent)!
let dest = CGImageDestinationCreateWithURL(URL(fileURLWithPath: a[2]) as CFURL, UTType.png.identifier as CFString, 1, nil)!
CGImageDestinationAddImage(dest, cg, nil)
CGImageDestinationFinalize(dest)
print("\(cg.width)x\(cg.height)")
