// Usage: bake figure <figure.png> <out.png>      – soft round edge baked into the alpha channel
//        bake lines  <lineart.png> <out.png>     – line art coloured bronze, soft edge baked in
// The intro then needs no CSS masks at runtime (masks are what makes Safari on iPhone slow while scrolling).
import Foundation
import CoreImage
import CoreImage.CIFilterBuiltins
import ImageIO
import UniformTypeIdentifiers

let a = CommandLine.arguments
let mode = a[1]
let input = CIImage(contentsOf: URL(fileURLWithPath: a[2]))!
let e = input.extent
let clear = CIImage(color: .clear).cropped(to: e)

// Radial falloff like CSS radial-gradient(closest-side, #000 74%, transparent 100%/96%).
func radial(_ inner: CGFloat, _ outer: CGFloat) -> CIImage {
    let g = CIFilter.radialGradient()
    g.center = CGPoint(x: e.midX, y: e.midY)
    let r = min(e.width, e.height) / 2
    g.radius0 = Float(r * inner); g.radius1 = Float(r * outer)
    g.color0 = CIColor(red: 1, green: 1, blue: 1, alpha: 1)
    g.color1 = CIColor(red: 1, green: 1, blue: 1, alpha: 0)
    return g.outputImage!.cropped(to: e)
}
func mask(_ img: CIImage, by m: CIImage) -> CIImage {
    let f = CIFilter.blendWithAlphaMask()
    f.inputImage = img; f.backgroundImage = clear; f.maskImage = m
    return f.outputImage!.cropped(to: e)
}

var out: CIImage
if mode == "figure" {
    out = mask(input, by: radial(0.74, 1.0))
} else {
    // Bronze gradient top → bottom, shown only where the line art has lines.
    let lg = CIFilter.linearGradient()
    lg.point0 = CGPoint(x: 0, y: e.maxY); lg.point1 = CGPoint(x: 0, y: e.minY)
    lg.color0 = CIColor(red: 0.965, green: 0.847, blue: 0.714)   // #f6d8b6
    lg.color1 = CIColor(red: 0.604, green: 0.384, blue: 0.220)   // #9a6238
    let bronze = lg.outputImage!.cropped(to: e)
    out = mask(mask(bronze, by: input), by: radial(0.74, 0.96))
}

let ctx = CIContext()
let cg = ctx.createCGImage(out, from: e, format: .RGBA8, colorSpace: CGColorSpace(name: CGColorSpace.sRGB))!
let dest = CGImageDestinationCreateWithURL(URL(fileURLWithPath: a[3]) as CFURL, UTType.png.identifier as CFString, 1, nil)!
CGImageDestinationAddImage(dest, cg, nil)
CGImageDestinationFinalize(dest)
print("\(cg.width)x\(cg.height)")
